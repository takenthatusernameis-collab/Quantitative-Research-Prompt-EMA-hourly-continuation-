# EMA Hourly Continuation — ZRO/USDT P12_55

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 915 |
| net_profit_factor | 0.7622 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1250 |
| gross_win_rate | 0.5301 |
| sharpe_ratio | -2.7407 |
| sortino_ratio | -1.2211 |
| max_drawdown | 0.7641 |
| cagr | -0.4405 |
| net_avg_win | 49.2404 |
| net_avg_loss | -72.2266 |
| avg_hold_time_bars | 8.6863 |
| exposure | 0.3890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
