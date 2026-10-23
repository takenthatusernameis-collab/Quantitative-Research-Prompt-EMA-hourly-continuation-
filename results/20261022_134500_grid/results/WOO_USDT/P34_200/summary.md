# EMA Hourly Continuation — WOO/USDT P34_200

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7773 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0851 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.5031 |
| sortino_ratio | -0.3792 |
| max_drawdown | 0.4138 |
| cagr | -0.1686 |
| net_avg_win | 78.4817 |
| net_avg_loss | -104.1190 |
| avg_hold_time_bars | 36.3354 |
| exposure | 0.5368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
