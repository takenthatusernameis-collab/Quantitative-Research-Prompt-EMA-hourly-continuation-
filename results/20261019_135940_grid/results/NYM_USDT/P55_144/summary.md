# EMA Hourly Continuation — NYM/USDT P55_144

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.2311 |
| net_win_rate | 0.3433 |
| gross_profit_factor | 0.5251 |
| gross_win_rate | 0.3841 |
| sharpe_ratio | -7.9490 |
| sortino_ratio | -2.4462 |
| max_drawdown | 0.9589 |
| cagr | -0.7194 |
| net_avg_win | 18.0141 |
| net_avg_loss | -40.7550 |
| avg_hold_time_bars | 12.0043 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
