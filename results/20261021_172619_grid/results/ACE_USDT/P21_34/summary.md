# EMA Hourly Continuation — ACE/USDT P21_34

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6332 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -2.6437 |
| sortino_ratio | -0.7887 |
| max_drawdown | 0.6142 |
| cagr | -0.3026 |
| net_avg_win | 48.1738 |
| net_avg_loss | -73.6677 |
| avg_hold_time_bars | 6.1126 |
| exposure | 0.1203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
