# EMA Hourly Continuation — BICO/USDT P12_55

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7425 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.3324 |
| sortino_ratio | -0.8695 |
| max_drawdown | 0.6401 |
| cagr | -0.3301 |
| net_avg_win | 54.7612 |
| net_avg_loss | -71.1977 |
| avg_hold_time_bars | 12.4632 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
