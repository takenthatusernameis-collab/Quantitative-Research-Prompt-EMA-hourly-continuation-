# EMA Hourly Continuation — XDC/USDT P55_144

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0122 |
| sortino_ratio | -0.5257 |
| max_drawdown | 0.4769 |
| cagr | -0.2138 |
| net_avg_win | 58.7003 |
| net_avg_loss | -86.0128 |
| avg_hold_time_bars | 13.7199 |
| exposure | 0.2070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
