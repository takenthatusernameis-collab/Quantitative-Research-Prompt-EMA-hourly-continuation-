# EMA Hourly Continuation — XYO/USDT P34_144

**Symbol:** XYO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6165 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -3.0979 |
| sortino_ratio | -0.8407 |
| max_drawdown | 0.6371 |
| cagr | -0.3228 |
| net_avg_win | 62.1018 |
| net_avg_loss | -79.2220 |
| avg_hold_time_bars | 21.7880 |
| exposure | 0.3628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
