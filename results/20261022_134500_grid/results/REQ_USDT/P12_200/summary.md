# EMA Hourly Continuation — REQ/USDT P12_200

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.4584 |
| net_win_rate | 0.4018 |
| gross_profit_factor | 0.7961 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -7.0771 |
| sortino_ratio | -2.5810 |
| max_drawdown | 0.9599 |
| cagr | -0.7213 |
| net_avg_win | 30.0748 |
| net_avg_loss | -44.0696 |
| avg_hold_time_bars | 20.5238 |
| exposure | 0.6269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
