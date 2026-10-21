# EMA Hourly Continuation — ERG/USDT P21_34

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7354 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -3.6541 |
| sortino_ratio | -0.8631 |
| max_drawdown | 0.6418 |
| cagr | -0.3295 |
| net_avg_win | 58.5223 |
| net_avg_loss | -80.2926 |
| avg_hold_time_bars | 5.6993 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
