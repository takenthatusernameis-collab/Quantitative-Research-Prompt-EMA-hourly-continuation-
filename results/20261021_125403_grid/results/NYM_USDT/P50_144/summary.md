# EMA Hourly Continuation — NYM/USDT P50_144

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.4628 |
| net_win_rate | 0.4208 |
| gross_profit_factor | 0.6874 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -3.4643 |
| sortino_ratio | -0.7913 |
| max_drawdown | 0.6310 |
| cagr | -0.3107 |
| net_avg_win | 48.0002 |
| net_avg_loss | -75.3597 |
| avg_hold_time_bars | 19.6100 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
