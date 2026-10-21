# EMA Hourly Continuation — STRK/USDT P8_200

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8582 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.7541 |
| sortino_ratio | -0.1802 |
| max_drawdown | 0.2207 |
| cagr | -0.0820 |
| net_avg_win | 83.5886 |
| net_avg_loss | -97.4008 |
| avg_hold_time_bars | 63.4179 |
| exposure | 0.8071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
