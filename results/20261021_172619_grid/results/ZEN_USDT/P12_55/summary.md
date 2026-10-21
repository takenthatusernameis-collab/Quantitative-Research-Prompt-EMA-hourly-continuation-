# EMA Hourly Continuation — ZEN/USDT P12_55

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.7183 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.6805 |
| sortino_ratio | -0.9651 |
| max_drawdown | 0.6813 |
| cagr | -0.3590 |
| net_avg_win | 56.2457 |
| net_avg_loss | -71.7153 |
| avg_hold_time_bars | 12.2179 |
| exposure | 0.3543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
