# EMA Hourly Continuation — SOL/USDT P8_89

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.8686 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1027 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.9273 |
| sortino_ratio | -0.3021 |
| max_drawdown | 0.3741 |
| cagr | -0.1330 |
| net_avg_win | 73.7273 |
| net_avg_loss | -95.0957 |
| avg_hold_time_bars | 24.7945 |
| exposure | 0.5759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
