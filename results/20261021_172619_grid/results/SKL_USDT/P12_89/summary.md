# EMA Hourly Continuation — SKL/USDT P12_89

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8725 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0593 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.0203 |
| sortino_ratio | -0.3221 |
| max_drawdown | 0.4663 |
| cagr | -0.1407 |
| net_avg_win | 87.3948 |
| net_avg_loss | -105.7058 |
| avg_hold_time_bars | 25.5735 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
