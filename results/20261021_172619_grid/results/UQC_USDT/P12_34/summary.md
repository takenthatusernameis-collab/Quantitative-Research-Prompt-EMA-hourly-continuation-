# EMA Hourly Continuation — UQC/USDT P12_34

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.3917 |
| net_win_rate | 0.3387 |
| gross_profit_factor | 0.6190 |
| gross_win_rate | 0.3546 |
| sharpe_ratio | -5.3352 |
| sortino_ratio | -1.3276 |
| max_drawdown | 0.7962 |
| cagr | -0.4660 |
| net_avg_win | 48.2575 |
| net_avg_loss | -63.0908 |
| avg_hold_time_bars | 36.6038 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
