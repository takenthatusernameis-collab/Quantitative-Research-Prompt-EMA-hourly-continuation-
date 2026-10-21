# EMA Hourly Continuation — IMX/USDT P12_34

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6966 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -2.7647 |
| sortino_ratio | -0.9689 |
| max_drawdown | 0.6943 |
| cagr | -0.3588 |
| net_avg_win | 53.5504 |
| net_avg_loss | -70.3044 |
| avg_hold_time_bars | 7.3950 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
