# EMA Hourly Continuation — PUNDIX/USDT P144_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.3880 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.3686 |
| sortino_ratio | -1.5160 |
| max_drawdown | 0.8512 |
| cagr | -0.5280 |
| net_avg_win | 30.5584 |
| net_avg_loss | -62.7185 |
| avg_hold_time_bars | 5.6423 |
| exposure | 0.1018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
