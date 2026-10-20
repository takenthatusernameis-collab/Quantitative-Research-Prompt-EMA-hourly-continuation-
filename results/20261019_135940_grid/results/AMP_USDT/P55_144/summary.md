# EMA Hourly Continuation — AMP/USDT P55_144

**Symbol:** AMP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.3256 |
| net_win_rate | 0.3755 |
| gross_profit_factor | 0.6040 |
| gross_win_rate | 0.3934 |
| sharpe_ratio | -8.3176 |
| sortino_ratio | -3.1476 |
| max_drawdown | 0.9822 |
| cagr | -0.7967 |
| net_avg_win | 17.3590 |
| net_avg_loss | -32.0615 |
| avg_hold_time_bars | 8.7331 |
| exposure | 0.2886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
