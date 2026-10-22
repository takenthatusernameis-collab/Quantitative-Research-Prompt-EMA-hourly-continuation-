# EMA Hourly Continuation — WIF/USDT P26_89

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -3.6857 |
| sortino_ratio | -1.3864 |
| max_drawdown | 0.8166 |
| cagr | -0.4833 |
| net_avg_win | 49.5104 |
| net_avg_loss | -67.5579 |
| avg_hold_time_bars | 9.4753 |
| exposure | 0.3054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
