# EMA Hourly Continuation — APT/USDT P20_144

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.9912 |
| net_win_rate | 0.5424 |
| gross_profit_factor | 1.1674 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | 0.0091 |
| sortino_ratio | 0.0023 |
| max_drawdown | 0.1804 |
| cagr | -0.0049 |
| net_avg_win | 85.6128 |
| net_avg_loss | -102.3700 |
| avg_hold_time_bars | 45.5153 |
| exposure | 0.6103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
