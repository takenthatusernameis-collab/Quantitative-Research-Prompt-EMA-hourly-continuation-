# EMA Hourly Continuation — AUCTION/USDT P20_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6263 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.6966 |
| sortino_ratio | -1.1547 |
| max_drawdown | 0.7622 |
| cagr | -0.4254 |
| net_avg_win | 55.3310 |
| net_avg_loss | -74.8814 |
| avg_hold_time_bars | 25.5272 |
| exposure | 0.5742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
