# EMA Hourly Continuation — ERG/USDT P55_144

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.7610 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -2.8540 |
| sortino_ratio | -0.7189 |
| max_drawdown | 0.5644 |
| cagr | -0.2818 |
| net_avg_win | 60.1966 |
| net_avg_loss | -77.6043 |
| avg_hold_time_bars | 16.0380 |
| exposure | 0.2304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
