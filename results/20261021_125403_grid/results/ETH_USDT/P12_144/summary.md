# EMA Hourly Continuation — ETH/USDT P12_144

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9503 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.4254 |
| sortino_ratio | -0.3175 |
| max_drawdown | 0.3449 |
| cagr | -0.1357 |
| net_avg_win | 69.3143 |
| net_avg_loss | -91.2512 |
| avg_hold_time_bars | 65.8189 |
| exposure | 0.7270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
