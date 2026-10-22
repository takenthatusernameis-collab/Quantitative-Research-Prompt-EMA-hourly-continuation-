# EMA Hourly Continuation — XDC/USDT P55_200

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.3773 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.7632 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -5.9452 |
| sortino_ratio | -1.8901 |
| max_drawdown | 0.9171 |
| cagr | -0.6251 |
| net_avg_win | 24.5315 |
| net_avg_loss | -49.9767 |
| avg_hold_time_bars | 12.3500 |
| exposure | 0.2919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
