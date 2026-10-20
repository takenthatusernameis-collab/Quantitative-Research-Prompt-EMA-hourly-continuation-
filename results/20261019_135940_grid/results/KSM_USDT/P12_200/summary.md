# EMA Hourly Continuation — KSM/USDT P12_200

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -2.8852 |
| sortino_ratio | -0.7392 |
| max_drawdown | 0.6152 |
| cagr | -0.3003 |
| net_avg_win | 63.2355 |
| net_avg_loss | -85.6946 |
| avg_hold_time_bars | 50.4716 |
| exposure | 0.7685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
