# EMA Hourly Continuation — GLM/USDT P20_100

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6641 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.9707 |
| sortino_ratio | -0.9768 |
| max_drawdown | 0.6880 |
| cagr | -0.3627 |
| net_avg_win | 53.3641 |
| net_avg_loss | -71.0157 |
| avg_hold_time_bars | 17.9215 |
| exposure | 0.4358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
