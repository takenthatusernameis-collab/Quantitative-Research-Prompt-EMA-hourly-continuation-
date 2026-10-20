# EMA Hourly Continuation — LQTY/USDT P21_144

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6686 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9085 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.4725 |
| sortino_ratio | -0.7214 |
| max_drawdown | 0.5832 |
| cagr | -0.2866 |
| net_avg_win | 56.4296 |
| net_avg_loss | -77.5895 |
| avg_hold_time_bars | 31.7313 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
