# EMA Hourly Continuation — XDC/USDT P8_89

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.7161 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0277 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.4972 |
| sortino_ratio | -0.8707 |
| max_drawdown | 0.6361 |
| cagr | -0.3279 |
| net_avg_win | 53.4254 |
| net_avg_loss | -75.6244 |
| avg_hold_time_bars | 18.5676 |
| exposure | 0.4996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
