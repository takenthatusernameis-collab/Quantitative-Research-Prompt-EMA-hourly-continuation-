# EMA Hourly Continuation — APT/USDT P34_200

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8281 |
| net_win_rate | 0.5357 |
| gross_profit_factor | 1.2047 |
| gross_win_rate | 0.5487 |
| sharpe_ratio | -0.9461 |
| sortino_ratio | -0.2350 |
| max_drawdown | 0.3058 |
| cagr | -0.1077 |
| net_avg_win | 72.6179 |
| net_avg_loss | -101.1892 |
| avg_hold_time_bars | 40.8214 |
| exposure | 0.5715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
