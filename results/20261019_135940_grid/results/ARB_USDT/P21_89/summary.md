# EMA Hourly Continuation — ARB/USDT P21_89

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -3.4413 |
| sortino_ratio | -1.2938 |
| max_drawdown | 0.7895 |
| cagr | -0.4589 |
| net_avg_win | 40.2307 |
| net_avg_loss | -62.2088 |
| avg_hold_time_bars | 11.2734 |
| exposure | 0.3618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
