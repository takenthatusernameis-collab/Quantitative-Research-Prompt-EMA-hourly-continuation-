# EMA Hourly Continuation — BDX/USDT P50_144

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.2417 |
| net_win_rate | 0.3037 |
| gross_profit_factor | 0.5965 |
| gross_win_rate | 0.3609 |
| sharpe_ratio | -14.8081 |
| sortino_ratio | -6.8215 |
| max_drawdown | 0.9999 |
| cagr | -0.9767 |
| net_avg_win | 10.7325 |
| net_avg_loss | -19.3638 |
| avg_hold_time_bars | 5.4417 |
| exposure | 0.2419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
