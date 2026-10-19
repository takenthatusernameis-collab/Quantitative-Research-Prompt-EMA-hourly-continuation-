# EMA Hourly Continuation — XDC/USDT P8_144

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8816 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -6.1556 |
| sortino_ratio | -2.2799 |
| max_drawdown | 0.9489 |
| cagr | -0.6911 |
| net_avg_win | 20.9445 |
| net_avg_loss | -41.1718 |
| avg_hold_time_bars | 19.1975 |
| exposure | 0.6274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
