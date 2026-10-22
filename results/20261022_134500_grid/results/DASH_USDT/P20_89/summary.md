# EMA Hourly Continuation — DASH/USDT P20_89

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.5182 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.9044 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -5.6541 |
| sortino_ratio | -2.1520 |
| max_drawdown | 0.9319 |
| cagr | -0.6457 |
| net_avg_win | 30.4618 |
| net_avg_loss | -47.4631 |
| avg_hold_time_bars | 11.4194 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
