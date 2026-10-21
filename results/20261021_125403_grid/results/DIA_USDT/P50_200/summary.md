# EMA Hourly Continuation — DIA/USDT P50_200

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8634 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0766 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.7479 |
| sortino_ratio | -0.1954 |
| max_drawdown | 0.3039 |
| cagr | -0.0882 |
| net_avg_win | 75.8988 |
| net_avg_loss | -96.2544 |
| avg_hold_time_bars | 26.0937 |
| exposure | 0.3908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
