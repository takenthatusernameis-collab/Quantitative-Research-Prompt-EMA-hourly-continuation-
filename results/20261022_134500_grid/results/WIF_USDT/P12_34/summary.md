# EMA Hourly Continuation — WIF/USDT P12_34

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1327 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 1.0229 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -7.2670 |
| sortino_ratio | -3.7280 |
| max_drawdown | 0.9900 |
| cagr | -0.8367 |
| net_avg_win | 31.7814 |
| net_avg_loss | -41.1435 |
| avg_hold_time_bars | 3.6549 |
| exposure | 0.2205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
