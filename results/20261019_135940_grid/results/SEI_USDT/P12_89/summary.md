# EMA Hourly Continuation — SEI/USDT P12_89

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7221 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0250 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -3.0115 |
| sortino_ratio | -1.0908 |
| max_drawdown | 0.7426 |
| cagr | -0.4047 |
| net_avg_win | 57.6872 |
| net_avg_loss | -79.1642 |
| avg_hold_time_bars | 18.7754 |
| exposure | 0.5624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
