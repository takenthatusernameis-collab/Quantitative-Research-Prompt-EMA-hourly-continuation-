# EMA Hourly Continuation — BOSON/USDT P55_89

**Symbol:** BOSON/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.8686 |
| sortino_ratio | -1.7980 |
| max_drawdown | 0.8856 |
| cagr | -0.5775 |
| net_avg_win | 35.1229 |
| net_avg_loss | -53.2934 |
| avg_hold_time_bars | 4.6069 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
