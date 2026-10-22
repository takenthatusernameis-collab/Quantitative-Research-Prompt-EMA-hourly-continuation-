# EMA Hourly Continuation — JTO/USDT P50_144

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5487 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -4.2376 |
| sortino_ratio | -1.3257 |
| max_drawdown | 0.8031 |
| cagr | -0.4656 |
| net_avg_win | 45.4554 |
| net_avg_loss | -61.8433 |
| avg_hold_time_bars | 11.6996 |
| exposure | 0.2638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
