# EMA Hourly Continuation — ERG/USDT P55_89

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.2475 |
| net_win_rate | 0.3424 |
| gross_profit_factor | 0.5264 |
| gross_win_rate | 0.3665 |
| sharpe_ratio | -9.5586 |
| sortino_ratio | -3.5228 |
| max_drawdown | 0.9886 |
| cagr | -0.8314 |
| net_avg_win | 14.3217 |
| net_avg_loss | -30.1300 |
| avg_hold_time_bars | 5.2398 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
