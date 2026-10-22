# EMA Hourly Continuation — STRK/USDT P55_89

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8748 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -5.7715 |
| sortino_ratio | -2.1173 |
| max_drawdown | 0.9300 |
| cagr | -0.6458 |
| net_avg_win | 30.2429 |
| net_avg_loss | -49.7228 |
| avg_hold_time_bars | 3.6353 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
