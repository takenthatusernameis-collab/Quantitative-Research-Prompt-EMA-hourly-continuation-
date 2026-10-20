# EMA Hourly Continuation — LPT/USDT P20_144

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6254 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -3.4812 |
| sortino_ratio | -1.1302 |
| max_drawdown | 0.7506 |
| cagr | -0.4186 |
| net_avg_win | 49.4759 |
| net_avg_loss | -68.7084 |
| avg_hold_time_bars | 21.1852 |
| exposure | 0.5200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
