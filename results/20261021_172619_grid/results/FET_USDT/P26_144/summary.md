# EMA Hourly Continuation — FET/USDT P26_144

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.9556 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1104 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.1965 |
| sortino_ratio | -0.0514 |
| max_drawdown | 0.1919 |
| cagr | -0.0286 |
| net_avg_win | 86.5653 |
| net_avg_loss | -102.2760 |
| avg_hold_time_bars | 32.0788 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
