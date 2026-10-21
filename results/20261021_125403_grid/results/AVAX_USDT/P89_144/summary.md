# EMA Hourly Continuation — AVAX/USDT P89_144

**Symbol:** AVAX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.8736 |
| sortino_ratio | -0.4064 |
| max_drawdown | 0.3912 |
| cagr | -0.1708 |
| net_avg_win | 69.3692 |
| net_avg_loss | -94.8541 |
| avg_hold_time_bars | 7.7478 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
