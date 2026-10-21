# EMA Hourly Continuation — SHIB/USDT P34_89

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6944 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.6238 |
| sortino_ratio | -0.7935 |
| max_drawdown | 0.6253 |
| cagr | -0.3048 |
| net_avg_win | 63.2598 |
| net_avg_loss | -84.4266 |
| avg_hold_time_bars | 9.7606 |
| exposure | 0.1983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
