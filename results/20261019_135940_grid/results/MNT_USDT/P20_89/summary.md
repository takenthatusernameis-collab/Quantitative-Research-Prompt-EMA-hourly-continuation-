# EMA Hourly Continuation — MNT/USDT P20_89

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.5013 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8934 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -5.1209 |
| sortino_ratio | -1.8070 |
| max_drawdown | 0.9022 |
| cagr | -0.5944 |
| net_avg_win | 30.5416 |
| net_avg_loss | -52.2467 |
| avg_hold_time_bars | 14.5415 |
| exposure | 0.4224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
