# EMA Hourly Continuation — XMR/USDT P12_20

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.5494 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -2.3015 |
| sortino_ratio | -0.4196 |
| max_drawdown | 0.3836 |
| cagr | -0.1753 |
| net_avg_win | 64.9566 |
| net_avg_loss | -93.5489 |
| avg_hold_time_bars | 4.2270 |
| exposure | 0.0313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
