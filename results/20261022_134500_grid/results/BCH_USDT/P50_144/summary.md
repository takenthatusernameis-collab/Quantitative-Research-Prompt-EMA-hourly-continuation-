# EMA Hourly Continuation — BCH/USDT P50_144

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.5281 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -4.6399 |
| sortino_ratio | -1.4757 |
| max_drawdown | 0.8405 |
| cagr | -0.5072 |
| net_avg_win | 40.4189 |
| net_avg_loss | -63.5550 |
| avg_hold_time_bars | 12.1203 |
| exposure | 0.2793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
