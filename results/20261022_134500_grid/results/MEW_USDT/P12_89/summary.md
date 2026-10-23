# EMA Hourly Continuation — MEW/USDT P12_89

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.5300 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.7515 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -5.1229 |
| sortino_ratio | -1.9075 |
| max_drawdown | 0.9100 |
| cagr | -0.6089 |
| net_avg_win | 32.0996 |
| net_avg_loss | -47.9130 |
| avg_hold_time_bars | 16.4458 |
| exposure | 0.5382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
