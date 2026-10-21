# EMA Hourly Continuation — ETH/USDT P21_144

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6163 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.2373 |
| sortino_ratio | -0.5076 |
| max_drawdown | 0.4675 |
| cagr | -0.2072 |
| net_avg_win | 60.6533 |
| net_avg_loss | -84.0532 |
| avg_hold_time_bars | 52.4724 |
| exposure | 0.6058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
