# EMA Hourly Continuation — STX/USDT P55_89

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.4538 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.7821 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -6.0274 |
| sortino_ratio | -2.1692 |
| max_drawdown | 0.9303 |
| cagr | -0.6501 |
| net_avg_win | 26.5287 |
| net_avg_loss | -47.2570 |
| avg_hold_time_bars | 3.7819 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
