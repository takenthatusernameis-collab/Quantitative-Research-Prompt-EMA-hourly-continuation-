# EMA Hourly Continuation — STX/USDT P20_89

**Symbol:** STX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7609 |
| net_win_rate | 0.4906 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -1.8275 |
| sortino_ratio | -0.5713 |
| max_drawdown | 0.5198 |
| cagr | -0.2316 |
| net_avg_win | 65.4721 |
| net_avg_loss | -82.8855 |
| avg_hold_time_bars | 16.8025 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
