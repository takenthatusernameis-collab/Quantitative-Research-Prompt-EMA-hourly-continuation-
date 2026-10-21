# EMA Hourly Continuation — JST/USDT P50_55

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.4274 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 1.0534 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -3.0076 |
| sortino_ratio | -0.5572 |
| max_drawdown | 0.5038 |
| cagr | -0.2349 |
| net_avg_win | 44.7010 |
| net_avg_loss | -100.9033 |
| avg_hold_time_bars | 6.2096 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
