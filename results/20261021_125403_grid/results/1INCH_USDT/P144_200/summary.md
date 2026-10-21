# EMA Hourly Continuation — 1INCH/USDT P144_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.7582 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1159 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -1.2031 |
| sortino_ratio | -0.2515 |
| max_drawdown | 0.2709 |
| cagr | -0.1090 |
| net_avg_win | 71.0579 |
| net_avg_loss | -106.1510 |
| avg_hold_time_bars | 7.1483 |
| exposure | 0.0679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
