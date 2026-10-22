# EMA Hourly Continuation — BCH/USDT P12_34

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1238 |
| net_profit_factor | 0.3435 |
| net_win_rate | 0.4136 |
| gross_profit_factor | 0.8030 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -11.4691 |
| sortino_ratio | -5.7235 |
| max_drawdown | 0.9994 |
| cagr | -0.9482 |
| net_avg_win | 10.2115 |
| net_avg_loss | -20.9675 |
| avg_hold_time_bars | 4.0323 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
