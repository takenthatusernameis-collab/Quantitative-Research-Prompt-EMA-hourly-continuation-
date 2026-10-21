# EMA Hourly Continuation — RUNE/USDT P20_89

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8049 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0256 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.2680 |
| sortino_ratio | -0.3610 |
| max_drawdown | 0.3926 |
| cagr | -0.1541 |
| net_avg_win | 70.4449 |
| net_avg_loss | -91.6207 |
| avg_hold_time_bars | 27.0662 |
| exposure | 0.4835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
